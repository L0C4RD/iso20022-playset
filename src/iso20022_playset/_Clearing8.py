# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NettingEligible1Code
from . import NonGuaranteedTrade4
from . import PartyIdentification253Choice
from . import YesNoIndicator

class Clearing8(base_types._BaseFieldType):

	__slots__ = ["_ClrSgmt", "_GrntedTrad", "_SttlmNetgElgblCd", "_TradCtrPtyId"]
	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if value is not None else base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification253Choice, False)

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification253Choice, False)

	@property
	def GrntedTrad(self):
		return self._GrntedTrad

	@GrntedTrad.setter
	def GrntedTrad(self, value):
		self._GrntedTrad = value if value is not None else base_types.UninitialisedField(self, 'GrntedTrad', YesNoIndicator, False)

	@GrntedTrad.deleter
	def GrntedTrad(self):
		del self._GrntedTrad
		self._GrntedTrad = base_types.UninitialisedField(self, 'GrntedTrad', YesNoIndicator, False)

	@property
	def SttlmNetgElgblCd(self):
		return self._SttlmNetgElgblCd

	@SttlmNetgElgblCd.setter
	def SttlmNetgElgblCd(self, value):
		self._SttlmNetgElgblCd = value if value is not None else base_types.UninitialisedField(self, 'SttlmNetgElgblCd', NettingEligible1Code, False)

	@SttlmNetgElgblCd.deleter
	def SttlmNetgElgblCd(self):
		del self._SttlmNetgElgblCd
		self._SttlmNetgElgblCd = base_types.UninitialisedField(self, 'SttlmNetgElgblCd', NettingEligible1Code, False)

	@property
	def TradCtrPtyId(self):
		return self._TradCtrPtyId

	@TradCtrPtyId.setter
	def TradCtrPtyId(self, value):
		self._TradCtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'TradCtrPtyId', NonGuaranteedTrade4, False)

	@TradCtrPtyId.deleter
	def TradCtrPtyId(self):
		del self._TradCtrPtyId
		self._TradCtrPtyId = base_types.UninitialisedField(self, 'TradCtrPtyId', NonGuaranteedTrade4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedTrad', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmNetgElgblCd', type=NettingEligible1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradCtrPtyId', type=NonGuaranteedTrade4, min=0, max=1, mutex_group=None, array=False),
	))