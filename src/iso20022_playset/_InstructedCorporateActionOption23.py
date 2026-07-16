# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceFormat11Choice
from . import CorporateActionEventDeadlines3
from . import CorporateActionOption30Choice
from . import DefaultProcessingOrStandingInstruction2Choice
from . import Exact3NumericText
from . import OptionInstructionDetails13
from . import SignedQuantityFormat10

class InstructedCorporateActionOption23(base_types._BaseFieldType):

	__slots__ = ["_DfltActn", "_EvtDdlns", "_InstdBal", "_OptnAccptdInstdBal", "_OptnCancInstrBal", "_OptnInstrDtls", "_OptnNb", "_OptnPdgInstrBal", "_OptnPrtctInstrBal", "_OptnRjctdInstrBal", "_OptnRtrdInstdBal", "_OptnTp"]
	@property
	def DfltActn(self):
		return self._DfltActn

	@DfltActn.setter
	def DfltActn(self, value):
		self._DfltActn = value if value is not None else base_types.UninitialisedField(self, 'DfltActn', DefaultProcessingOrStandingInstruction2Choice, False)

	@DfltActn.deleter
	def DfltActn(self):
		del self._DfltActn
		self._DfltActn = base_types.UninitialisedField(self, 'DfltActn', DefaultProcessingOrStandingInstruction2Choice, False)

	@property
	def EvtDdlns(self):
		return self._EvtDdlns

	@EvtDdlns.setter
	def EvtDdlns(self, value):
		self._EvtDdlns = value if value is not None else base_types.UninitialisedField(self, 'EvtDdlns', CorporateActionEventDeadlines3, False)

	@EvtDdlns.deleter
	def EvtDdlns(self):
		del self._EvtDdlns
		self._EvtDdlns = base_types.UninitialisedField(self, 'EvtDdlns', CorporateActionEventDeadlines3, False)

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if value is not None else base_types.UninitialisedField(self, 'InstdBal', BalanceFormat11Choice, False)

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = base_types.UninitialisedField(self, 'InstdBal', BalanceFormat11Choice, False)

	@property
	def OptnAccptdInstdBal(self):
		return self._OptnAccptdInstdBal

	@OptnAccptdInstdBal.setter
	def OptnAccptdInstdBal(self, value):
		self._OptnAccptdInstdBal = value if value is not None else base_types.UninitialisedField(self, 'OptnAccptdInstdBal', SignedQuantityFormat10, False)

	@OptnAccptdInstdBal.deleter
	def OptnAccptdInstdBal(self):
		del self._OptnAccptdInstdBal
		self._OptnAccptdInstdBal = base_types.UninitialisedField(self, 'OptnAccptdInstdBal', SignedQuantityFormat10, False)

	@property
	def OptnCancInstrBal(self):
		return self._OptnCancInstrBal

	@OptnCancInstrBal.setter
	def OptnCancInstrBal(self, value):
		self._OptnCancInstrBal = value if value is not None else base_types.UninitialisedField(self, 'OptnCancInstrBal', SignedQuantityFormat10, False)

	@OptnCancInstrBal.deleter
	def OptnCancInstrBal(self):
		del self._OptnCancInstrBal
		self._OptnCancInstrBal = base_types.UninitialisedField(self, 'OptnCancInstrBal', SignedQuantityFormat10, False)

	@property
	def OptnInstrDtls(self):
		return self._OptnInstrDtls

	@OptnInstrDtls.setter
	def OptnInstrDtls(self, value):
		self._OptnInstrDtls = value if value is not None else base_types.UninitialisedField(self, 'OptnInstrDtls', OptionInstructionDetails13, True)

	@OptnInstrDtls.deleter
	def OptnInstrDtls(self):
		del self._OptnInstrDtls
		self._OptnInstrDtls = base_types.UninitialisedField(self, 'OptnInstrDtls', OptionInstructionDetails13, True)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnPdgInstrBal(self):
		return self._OptnPdgInstrBal

	@OptnPdgInstrBal.setter
	def OptnPdgInstrBal(self, value):
		self._OptnPdgInstrBal = value if value is not None else base_types.UninitialisedField(self, 'OptnPdgInstrBal', SignedQuantityFormat10, False)

	@OptnPdgInstrBal.deleter
	def OptnPdgInstrBal(self):
		del self._OptnPdgInstrBal
		self._OptnPdgInstrBal = base_types.UninitialisedField(self, 'OptnPdgInstrBal', SignedQuantityFormat10, False)

	@property
	def OptnPrtctInstrBal(self):
		return self._OptnPrtctInstrBal

	@OptnPrtctInstrBal.setter
	def OptnPrtctInstrBal(self, value):
		self._OptnPrtctInstrBal = value if value is not None else base_types.UninitialisedField(self, 'OptnPrtctInstrBal', SignedQuantityFormat10, False)

	@OptnPrtctInstrBal.deleter
	def OptnPrtctInstrBal(self):
		del self._OptnPrtctInstrBal
		self._OptnPrtctInstrBal = base_types.UninitialisedField(self, 'OptnPrtctInstrBal', SignedQuantityFormat10, False)

	@property
	def OptnRjctdInstrBal(self):
		return self._OptnRjctdInstrBal

	@OptnRjctdInstrBal.setter
	def OptnRjctdInstrBal(self, value):
		self._OptnRjctdInstrBal = value if value is not None else base_types.UninitialisedField(self, 'OptnRjctdInstrBal', SignedQuantityFormat10, False)

	@OptnRjctdInstrBal.deleter
	def OptnRjctdInstrBal(self):
		del self._OptnRjctdInstrBal
		self._OptnRjctdInstrBal = base_types.UninitialisedField(self, 'OptnRjctdInstrBal', SignedQuantityFormat10, False)

	@property
	def OptnRtrdInstdBal(self):
		return self._OptnRtrdInstdBal

	@OptnRtrdInstdBal.setter
	def OptnRtrdInstdBal(self, value):
		self._OptnRtrdInstdBal = value if value is not None else base_types.UninitialisedField(self, 'OptnRtrdInstdBal', SignedQuantityFormat10, False)

	@OptnRtrdInstdBal.deleter
	def OptnRtrdInstdBal(self):
		del self._OptnRtrdInstdBal
		self._OptnRtrdInstdBal = base_types.UninitialisedField(self, 'OptnRtrdInstdBal', SignedQuantityFormat10, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption30Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption30Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltActn', type=DefaultProcessingOrStandingInstruction2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDdlns', type=CorporateActionEventDeadlines3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=BalanceFormat11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnAccptdInstdBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnCancInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnInstrDtls', type=OptionInstructionDetails13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPdgInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPrtctInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnRjctdInstrBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnRtrdInstdBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption30Choice, min=1, max=1, mutex_group=None, array=False),
	))