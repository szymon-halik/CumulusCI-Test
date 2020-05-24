from cumulusci.tasks.salesforce import BaseSalesforceApiTask
from cumulusci.tasks.salesforce import BaseSalesforceToolingApiTask

class ListContacts(BaseSalesforceApiTask):

    def _run_task(self):
        res = self.sf.query('Select Id, FirstName, LastName from Contact LIMIT 10')
        for contact in res['records']:
            self.logger.info('{Id}: {FirstName} {LastName}'.format(**contact))

class ListApexClasses(BaseSalesforceToolingApiTask):

    def _run_task(self):
        res = self.tooling.query('Select Id, Name, NamespacePrefix from ApexClass LIMIT 10')
        for apexclass in res['records']:
            self.logger.info('{Id}: [{NamespacePrefix}] {Name}'.format(**apexclass))