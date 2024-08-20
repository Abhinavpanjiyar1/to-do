import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/Users/abhinavpanjiyar/PycharmProjects/pythonProject1/extractor app/005 compressed.zip",
                    "/Users/abhinavpanjiyar/PycharmProjects/pythonProject1/extractor app")
