# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NettingEligible1Code import NettingEligible1Code
from ._NonGuaranteedTrade4 import NonGuaranteedTrade4
from ._PartyIdentification253Choice import PartyIdentification253Choice
from ._YesNoIndicator import YesNoIndicator

class Clearing8(base_types._BaseFieldType):

	__slots__ = ["_ClrSgmt", "_GrntedTrad", "_SttlmNetgElgblCd", "_TradCtrPtyId"]
	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != base_types.auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

	@property
	def GrntedTrad(self):
		return self._GrntedTrad

	@GrntedTrad.setter
	def GrntedTrad(self, value):
		self._GrntedTrad = value if type(value) != base_types.auto else self.make_default("GrntedTrad")

	@GrntedTrad.deleter
	def GrntedTrad(self):
		del self._GrntedTrad
		self._GrntedTrad = None

	@property
	def SttlmNetgElgblCd(self):
		return self._SttlmNetgElgblCd

	@SttlmNetgElgblCd.setter
	def SttlmNetgElgblCd(self, value):
		self._SttlmNetgElgblCd = value if type(value) != base_types.auto else self.make_default("SttlmNetgElgblCd")

	@SttlmNetgElgblCd.deleter
	def SttlmNetgElgblCd(self):
		del self._SttlmNetgElgblCd
		self._SttlmNetgElgblCd = None

	@property
	def TradCtrPtyId(self):
		return self._TradCtrPtyId

	@TradCtrPtyId.setter
	def TradCtrPtyId(self, value):
		self._TradCtrPtyId = value if type(value) != base_types.auto else self.make_default("TradCtrPtyId")

	@TradCtrPtyId.deleter
	def TradCtrPtyId(self):
		del self._TradCtrPtyId
		self._TradCtrPtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedTrad', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmNetgElgblCd', type=NettingEligible1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradCtrPtyId', type=NonGuaranteedTrade4, min=0, max=1, mutex_group=None, array=False),
	))