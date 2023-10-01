import os
import argparse
import shotgun_api3

# Shotgun server and authentication details
SHOTGUN_SERVER = "https://your-shotgun-site-url.com"
SCRIPT_NAME = "your_script_name"
SCRIPT_KEY = "your_script_key"

sg = shotgun_api3.Shotgun(SHOTGUN_SERVER, script_name=SCRIPT_NAME, api_key=SCRIPT_KEY)

def downloadAttachments(noteId):
    # Find the Note entity by its ID
    note = sg.find_one("Note", [["id", "is", noteId]], ["attachments", "subject"])

    if note:
        noteSubject = note["subject"]
        print(f"Downloading attachments for Note '{noteSubject}'...")

        attachments = note.get("attachments", [])
        if not attachments:
            print("No attachments found for this Note.")
            return

        for attachment in attachments:
            attachmentId = attachment["id"]
            attachmentType = attachment["type"]
            attachmentNaming = attachment["name"]

           # Download the attachment
            attachmentEntity = sg.find_one(attachmentType, [["id", "is", attachmentId]])
            attachmentName = attachmentEntity.get("name", f"{attachmentNaming}")
            filePath = os.path.join(os.getcwd(), attachmentName)

            sg.download_attachment(attachmentEntity, file_path=filePath)
            print(f"Downloaded: '{attachmentName}'")

def main():
    parser = argparse.ArgumentParser(description="Download attachments, annotations, and notes from Shotgun Notes.")
    parser.add_argument("noteId", type=int, help="ID of the Shotgun Note")

    args = parser.parse_args()
    noteId = args.noteId
    downloadAttachments(noteId)

if __name__ == "__main__":
    main()
