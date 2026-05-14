from . import base_types
from ._AccountIdentification38Choice import AccountIdentification38Choice
from ._InvoiceTotals7 import InvoiceTotals7
from ._ServiceCategoryTotals7 import ServiceCategoryTotals7

class InvoiceTotals8(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_InvcTtls", "_SvcCtgyTtls"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def InvcTtls(self):
		return self._InvcTtls

	@InvcTtls.setter
	def InvcTtls(self, value):
		self._InvcTtls = value if type(value) != base_types.auto else self.make_default("InvcTtls")

	@InvcTtls.deleter
	def InvcTtls(self):
		del self._InvcTtls
		self._InvcTtls = None

	@property
	def SvcCtgyTtls(self):
		return self._SvcCtgyTtls

	@SvcCtgyTtls.setter
	def SvcCtgyTtls(self, value):
		self._SvcCtgyTtls = value if type(value) != base_types.auto else self.make_default("SvcCtgyTtls")

	@SvcCtgyTtls.deleter
	def SvcCtgyTtls(self):
		del self._SvcCtgyTtls
		self._SvcCtgyTtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification38Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcTtls', type=InvoiceTotals7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCtgyTtls', type=ServiceCategoryTotals7, min=1, max=None, mutex_group=None, array=True),
	))

