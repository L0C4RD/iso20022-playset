from . import base_types
import FinancialInstitutionIdentification4Choice
import CashAccount24

class SettlementTerms3(base_types._BaseFieldType):

	__slots__ = ["_CdtrAgt", "_CdtrAcct"]
	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrAgt', type=FinancialInstitutionIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount24, min=1, max=1, mutex_group=None, array=False),
	))

