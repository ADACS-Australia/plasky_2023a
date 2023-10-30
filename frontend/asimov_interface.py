import configparser


def check_asimov():
    """
    Called from settings.py to verify that Asimov is importable and returns the current Asimov Project
    """
    try:
        import asimov
        from asimov import config as asimov_config
        print("Asimov version found:", asimov.__version__)
        try:
            project_name = asimov_config.get("project", "name")
            print("Current Asimov project:", project_name)
            return project_name
        except configparser.NoOptionError:
            raise Exception("No Asimov project configured in this directory. Have you run `asimov init`?")
    except ImportError:
        raise Exception("Unable to find Asimov, is it installed?")