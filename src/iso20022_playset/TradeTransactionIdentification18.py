import base_types
import PartyIdentification236Choice
import Max52Text
import OrganisationIdentification15Choice
import MasterAgreement7

class TradeTransactionIdentification18(base_types._BaseFieldType):

	__slots__ = ["_RptgCtrPty", "_OthrCtrPty", "_UnqTradIdr", "_MstrAgrmt"]
	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=PartyIdentification236Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement7, min=0, max=1, mutex_group=None, array=False),
	))

