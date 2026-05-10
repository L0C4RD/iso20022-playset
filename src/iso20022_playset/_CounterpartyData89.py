from . import base_types
from ._CounterpartyIdentification12 import CounterpartyIdentification12
from ._CounterpartyIdentification11 import CounterpartyIdentification11
from ._TransactionCounterpartyData11 import TransactionCounterpartyData11
from ._OrganisationIdentification15Choice import OrganisationIdentification15Choice

class CounterpartyData89(base_types._BaseFieldType):

	__slots__ = ["_RptgCtrPty", "_OthrPtyData", "_NttyRspnsblForRpt", "_OthrCtrPty"]
	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != base_types.auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def OthrPtyData(self):
		return self._OthrPtyData

	@OthrPtyData.setter
	def OthrPtyData(self, value):
		self._OthrPtyData = value if type(value) != base_types.auto else self.make_default("OthrPtyData")

	@OthrPtyData.deleter
	def OthrPtyData(self):
		del self._OthrPtyData
		self._OthrPtyData = None

	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if type(value) != base_types.auto else self.make_default("NttyRspnsblForRpt")

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = None

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != base_types.auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgCtrPty', type=CounterpartyIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPtyData', type=TransactionCounterpartyData11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=CounterpartyIdentification12, min=1, max=1, mutex_group=None, array=False),
	))

