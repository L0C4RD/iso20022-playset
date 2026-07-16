# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MasterAgreement7
from . import Max140Text
from . import Max52Text
from . import OrganisationIdentification15Choice
from . import PartyIdentification236Choice

class TradeTransactionIdentification20(base_types._BaseFieldType):

	__slots__ = ["_AgtLndr", "_MstrAgrmt", "_NttyRspnsblForRpt", "_OthrCtrPty", "_RptgCtrPty", "_TechRcrdId", "_TrptyAgt", "_UnqTradIdr"]
	@property
	def AgtLndr(self):
		return self._AgtLndr

	@AgtLndr.setter
	def AgtLndr(self, value):
		self._AgtLndr = value if value is not None else base_types.UninitialisedField(self, 'AgtLndr', OrganisationIdentification15Choice, False)

	@AgtLndr.deleter
	def AgtLndr(self):
		del self._AgtLndr
		self._AgtLndr = base_types.UninitialisedField(self, 'AgtLndr', OrganisationIdentification15Choice, False)

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement7, False)

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement7, False)

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
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', PartyIdentification236Choice, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', PartyIdentification236Choice, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', OrganisationIdentification15Choice, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', OrganisationIdentification15Choice, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', OrganisationIdentification15Choice, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', OrganisationIdentification15Choice, False)

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtLndr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=PartyIdentification236Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
	))