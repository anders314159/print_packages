import pkg_resources


class PrintsPackages:
    def perform(self):
        packages = sorted(["%s==%s" % (i.key, i.version) for i in pkg_resources.working_set])
        for package in packages:
            print(package)
        return packages
