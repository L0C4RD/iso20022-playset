# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveringPartiesAndAccount22
from . import PartyIdentification253Choice
from . import ReceivingPartiesAndAccount22

class NonGuaranteedTrade4(base_types._BaseFieldType):

	__slots__ = ["_DlvrgPties", "_RcvgPties", "_TradCtrPtyClrMmbId", "_TradCtrPtyMmbId"]
	@property
	def DlvrgPties(self):
		return self._DlvrgPties

	@DlvrgPties.setter
	def DlvrgPties(self, value):
		self._DlvrgPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgPties', DeliveringPartiesAndAccount22, False)

	@DlvrgPties.deleter
	def DlvrgPties(self):
		del self._DlvrgPties
		self._DlvrgPties = base_types.UninitialisedField(self, 'DlvrgPties', DeliveringPartiesAndAccount22, False)

	@property
	def RcvgPties(self):
		return self._RcvgPties

	@RcvgPties.setter
	def RcvgPties(self, value):
		self._RcvgPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgPties', ReceivingPartiesAndAccount22, False)

	@RcvgPties.deleter
	def RcvgPties(self):
		del self._RcvgPties
		self._RcvgPties = base_types.UninitialisedField(self, 'RcvgPties', ReceivingPartiesAndAccount22, False)

	@property
	def TradCtrPtyClrMmbId(self):
		return self._TradCtrPtyClrMmbId

	@TradCtrPtyClrMmbId.setter
	def TradCtrPtyClrMmbId(self, value):
		self._TradCtrPtyClrMmbId = value if value is not None else base_types.UninitialisedField(self, 'TradCtrPtyClrMmbId', PartyIdentification253Choice, False)

	@TradCtrPtyClrMmbId.deleter
	def TradCtrPtyClrMmbId(self):
		del self._TradCtrPtyClrMmbId
		self._TradCtrPtyClrMmbId = base_types.UninitialisedField(self, 'TradCtrPtyClrMmbId', PartyIdentification253Choice, False)

	@property
	def TradCtrPtyMmbId(self):
		return self._TradCtrPtyMmbId

	@TradCtrPtyMmbId.setter
	def TradCtrPtyMmbId(self, value):
		self._TradCtrPtyMmbId = value if value is not None else base_types.UninitialisedField(self, 'TradCtrPtyMmbId', PartyIdentification253Choice, False)

	@TradCtrPtyMmbId.deleter
	def TradCtrPtyMmbId(self):
		del self._TradCtrPtyMmbId
		self._TradCtrPtyMmbId = base_types.UninitialisedField(self, 'TradCtrPtyMmbId', PartyIdentification253Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgPties', type=DeliveringPartiesAndAccount22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgPties', type=ReceivingPartiesAndAccount22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradCtrPtyClrMmbId', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradCtrPtyMmbId', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
	))