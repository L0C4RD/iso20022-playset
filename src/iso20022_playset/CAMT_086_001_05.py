from . import base_types
from .BankServicesBillingStatementV05 import BankServicesBillingStatementV05

class CAMT_086_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BkSvcsBllgStmt"]
		@property
		def BkSvcsBllgStmt(self):
			return self._BkSvcsBllgStmt

		@BkSvcsBllgStmt.setter
		def BkSvcsBllgStmt(self, value):
			self._BkSvcsBllgStmt = value if type(value) != auto else self.make_default("BkSvcsBllgStmt")

		@BkSvcsBllgStmt.deleter
		def BkSvcsBllgStmt(self):
			del self._BkSvcsBllgStmt
			self._BkSvcsBllgStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkSvcsBllgStmt', type=BankServicesBillingStatementV05, min=1, max=1, mutex_group=None, array=False),
		))

