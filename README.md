**"# ShotgridProgrammings" **

Download Shotgun Attachment CLI Tool Documentation

**Introduction**
The "Download Shotgun Attachment CLI Tool" is a command-line utility that allows you to easily download attachments, annotations, and notes from Shotgun (ShotGrid) entities. This tool simplifies the process of retrieving files associated with specific entities, making it useful for Shotgun users and developers.

**Configuration**
The tool does not require any configuration. However, you should ensure that you have valid authentication credentials for your Shotgun instance, which may involve setting up a Shotgun script and obtaining an API key.

**Troubleshooting**
If you encounter any issues or errors while using the tool, refer to the following troubleshooting tips:

Authentication Error: Ensure that you have provided valid Shotgun server URL, script name, and script key in the script's configuration.

Entity Not Found: Verify that the specified entity type and entity IDs exist in your Shotgun instance.

Missing Attachments: If attachments are missing in the download, check that the Shotgun entity is correctly linked to the attachments.

Frequently Asked Questions **(FAQs)**
Q: Can I download attachments from multiple entities at once?
Yes, you can specify multiple entity IDs separated by spaces when using the tool. For example: python download_shotgun_attachments.py Version 123 456.

Q: What file formats are supported for download?
The tool supports downloading attachments in various formats, including images (e.g., .jpg, .png) and movies (e.g., .mov).

**Known Limitations**
The tool may not handle attachments with special characters in their names well. Ensure that attachment names in Shotgun do not contain problematic characters.
Contributing
Contributions to this tool are welcome. If you'd like to contribute, please follow the guidelines in the Contributing document.

License
This tool is licensed under the MIT License.

Author

Tejaswi Dongre
Version History
Version 1.0.0 (Date)
Conclusion
The "Download Shotgun Attachment CLI Tool" simplifies the process of downloading attachments, annotations, and notes from Shotgun entities. It provides an efficient way to manage your Shotgun data and files.

References
Shotgun API Documentation

