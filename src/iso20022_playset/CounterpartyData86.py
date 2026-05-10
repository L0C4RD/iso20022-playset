import base_types
import TrueFalseIndicator
import OrganisationIdentification15Choice
import CounterpartyIdentification10

class CounterpartyData86(base_types._BaseFieldType):

	__slots__ = ["_TrptyAgt", "_RptgCtrPty", "_OthrCtrPty", "_AgtLndr"]
	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if type(value) != auto else self.make_default("TrptyAgt")

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = None

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
	def AgtLndr(self):
		return self._AgtLndr

	@AgtLndr.setter
	def AgtLndr(self, value):
		self._AgtLndr = value if type(value) != auto else self.make_default("AgtLndr")

	@AgtLndr.deleter
	def AgtLndr(self):
		del self._AgtLndr
		self._AgtLndr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrptyAgt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=CounterpartyIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtLndr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

