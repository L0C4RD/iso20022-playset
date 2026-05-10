from . import base_types
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._YesNoIndicator import YesNoIndicator

class IssuanceAccount2(base_types._BaseFieldType):

	__slots__ = ["_PmryAcctInd", "_IssncAcct"]
	@property
	def PmryAcctInd(self):
		return self._PmryAcctInd

	@PmryAcctInd.setter
	def PmryAcctInd(self, value):
		self._PmryAcctInd = value if type(value) != base_types.auto else self.make_default("PmryAcctInd")

	@PmryAcctInd.deleter
	def PmryAcctInd(self):
		del self._PmryAcctInd
		self._PmryAcctInd = None

	@property
	def IssncAcct(self):
		return self._IssncAcct

	@IssncAcct.setter
	def IssncAcct(self, value):
		self._IssncAcct = value if type(value) != base_types.auto else self.make_default("IssncAcct")

	@IssncAcct.deleter
	def IssncAcct(self):
		del self._IssncAcct
		self._IssncAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmryAcctInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
	))

