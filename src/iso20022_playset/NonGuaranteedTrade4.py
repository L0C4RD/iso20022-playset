import base_types
import DeliveringPartiesAndAccount22
import ReceivingPartiesAndAccount22
import PartyIdentification253Choice

class NonGuaranteedTrade4(base_types._BaseFieldType):

	__slots__ = ["_DlvrgPties", "_TradCtrPtyClrMmbId", "_RcvgPties", "_TradCtrPtyMmbId"]
	@property
	def DlvrgPties(self):
		return self._DlvrgPties

	@DlvrgPties.setter
	def DlvrgPties(self, value):
		self._DlvrgPties = value if type(value) != auto else self.make_default("DlvrgPties")

	@DlvrgPties.deleter
	def DlvrgPties(self):
		del self._DlvrgPties
		self._DlvrgPties = None

	@property
	def TradCtrPtyClrMmbId(self):
		return self._TradCtrPtyClrMmbId

	@TradCtrPtyClrMmbId.setter
	def TradCtrPtyClrMmbId(self, value):
		self._TradCtrPtyClrMmbId = value if type(value) != auto else self.make_default("TradCtrPtyClrMmbId")

	@TradCtrPtyClrMmbId.deleter
	def TradCtrPtyClrMmbId(self):
		del self._TradCtrPtyClrMmbId
		self._TradCtrPtyClrMmbId = None

	@property
	def RcvgPties(self):
		return self._RcvgPties

	@RcvgPties.setter
	def RcvgPties(self, value):
		self._RcvgPties = value if type(value) != auto else self.make_default("RcvgPties")

	@RcvgPties.deleter
	def RcvgPties(self):
		del self._RcvgPties
		self._RcvgPties = None

	@property
	def TradCtrPtyMmbId(self):
		return self._TradCtrPtyMmbId

	@TradCtrPtyMmbId.setter
	def TradCtrPtyMmbId(self, value):
		self._TradCtrPtyMmbId = value if type(value) != auto else self.make_default("TradCtrPtyMmbId")

	@TradCtrPtyMmbId.deleter
	def TradCtrPtyMmbId(self):
		del self._TradCtrPtyMmbId
		self._TradCtrPtyMmbId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgPties', type=DeliveringPartiesAndAccount22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradCtrPtyClrMmbId', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgPties', type=ReceivingPartiesAndAccount22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradCtrPtyMmbId', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
	))

