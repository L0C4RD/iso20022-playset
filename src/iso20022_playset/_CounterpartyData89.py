# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyIdentification11
from . import CounterpartyIdentification12
from . import OrganisationIdentification15Choice
from . import TransactionCounterpartyData11

class CounterpartyData89(base_types._BaseFieldType):

	__slots__ = ["_NttyRspnsblForRpt", "_OthrCtrPty", "_OthrPtyData", "_RptgCtrPty"]
	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if value is not None else base_types.UninitialisedField(self, 'NttyRspnsblForRpt', OrganisationIdentification15Choice, False)

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = base_types.UninitialisedField(self, 'NttyRspnsblForRpt', OrganisationIdentification15Choice, False)

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', CounterpartyIdentification12, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', CounterpartyIdentification12, False)

	@property
	def OthrPtyData(self):
		return self._OthrPtyData

	@OthrPtyData.setter
	def OthrPtyData(self, value):
		self._OthrPtyData = value if value is not None else base_types.UninitialisedField(self, 'OthrPtyData', TransactionCounterpartyData11, False)

	@OthrPtyData.deleter
	def OthrPtyData(self):
		del self._OthrPtyData
		self._OthrPtyData = base_types.UninitialisedField(self, 'OthrPtyData', TransactionCounterpartyData11, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', CounterpartyIdentification11, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', CounterpartyIdentification11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=CounterpartyIdentification12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPtyData', type=TransactionCounterpartyData11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=CounterpartyIdentification11, min=1, max=1, mutex_group=None, array=False),
	))