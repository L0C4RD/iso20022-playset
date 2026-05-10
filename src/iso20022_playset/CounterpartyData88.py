import base_types
import ISODateTime
import CounterpartyData89
import OrganisationIdentification15Choice

class CounterpartyData88(base_types._BaseFieldType):

	__slots__ = ["_RptgDtTm", "_CtrPty", "_RptSubmitgNtty"]
	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if type(value) != auto else self.make_default("RptgDtTm")

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = None

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	@property
	def RptSubmitgNtty(self):
		return self._RptSubmitgNtty

	@RptSubmitgNtty.setter
	def RptSubmitgNtty(self, value):
		self._RptSubmitgNtty = value if type(value) != auto else self.make_default("RptSubmitgNtty")

	@RptSubmitgNtty.deleter
	def RptSubmitgNtty(self):
		del self._RptSubmitgNtty
		self._RptSubmitgNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=CounterpartyData89, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSubmitgNtty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
	))

