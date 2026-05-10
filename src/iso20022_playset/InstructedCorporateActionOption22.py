from . import base_types
from .DefaultProcessingOrStandingInstruction2Choice import DefaultProcessingOrStandingInstruction2Choice
from .CorporateActionOption36Choice import CorporateActionOption36Choice
from .OptionInstructionDetails12 import OptionInstructionDetails12
from .BalanceFormat14Choice import BalanceFormat14Choice
from .Exact3NumericText import Exact3NumericText
from .SignedQuantityFormat16 import SignedQuantityFormat16
from .CorporateActionEventDeadlines4 import CorporateActionEventDeadlines4
from .SignedQuantityFormat13 import SignedQuantityFormat13

class InstructedCorporateActionOption22(base_types._BaseFieldType):

	__slots__ = ["_OptnNb", "_DfltActn", "_InstdBal", "_OptnTp", "_OptnCancInstrBal", "_OptnRjctdInstrBal", "_OptnPrtctInstrBal", "_EvtDdlns", "_OptnInstrDtls", "_OptnAccptdInstdBal", "_OptnPdgInstrBal", "_OptnRtrdInstdBal"]
	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def DfltActn(self):
		return self._DfltActn

	@DfltActn.setter
	def DfltActn(self, value):
		self._DfltActn = value if type(value) != auto else self.make_default("DfltActn")

	@DfltActn.deleter
	def DfltActn(self):
		del self._DfltActn
		self._DfltActn = None

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if type(value) != auto else self.make_default("InstdBal")

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def OptnCancInstrBal(self):
		return self._OptnCancInstrBal

	@OptnCancInstrBal.setter
	def OptnCancInstrBal(self, value):
		self._OptnCancInstrBal = value if type(value) != auto else self.make_default("OptnCancInstrBal")

	@OptnCancInstrBal.deleter
	def OptnCancInstrBal(self):
		del self._OptnCancInstrBal
		self._OptnCancInstrBal = None

	@property
	def OptnRjctdInstrBal(self):
		return self._OptnRjctdInstrBal

	@OptnRjctdInstrBal.setter
	def OptnRjctdInstrBal(self, value):
		self._OptnRjctdInstrBal = value if type(value) != auto else self.make_default("OptnRjctdInstrBal")

	@OptnRjctdInstrBal.deleter
	def OptnRjctdInstrBal(self):
		del self._OptnRjctdInstrBal
		self._OptnRjctdInstrBal = None

	@property
	def OptnPrtctInstrBal(self):
		return self._OptnPrtctInstrBal

	@OptnPrtctInstrBal.setter
	def OptnPrtctInstrBal(self, value):
		self._OptnPrtctInstrBal = value if type(value) != auto else self.make_default("OptnPrtctInstrBal")

	@OptnPrtctInstrBal.deleter
	def OptnPrtctInstrBal(self):
		del self._OptnPrtctInstrBal
		self._OptnPrtctInstrBal = None

	@property
	def EvtDdlns(self):
		return self._EvtDdlns

	@EvtDdlns.setter
	def EvtDdlns(self, value):
		self._EvtDdlns = value if type(value) != auto else self.make_default("EvtDdlns")

	@EvtDdlns.deleter
	def EvtDdlns(self):
		del self._EvtDdlns
		self._EvtDdlns = None

	@property
	def OptnInstrDtls(self):
		return self._OptnInstrDtls

	@OptnInstrDtls.setter
	def OptnInstrDtls(self, value):
		self._OptnInstrDtls = value if type(value) != auto else self.make_default("OptnInstrDtls")

	@OptnInstrDtls.deleter
	def OptnInstrDtls(self):
		del self._OptnInstrDtls
		self._OptnInstrDtls = None

	@property
	def OptnAccptdInstdBal(self):
		return self._OptnAccptdInstdBal

	@OptnAccptdInstdBal.setter
	def OptnAccptdInstdBal(self, value):
		self._OptnAccptdInstdBal = value if type(value) != auto else self.make_default("OptnAccptdInstdBal")

	@OptnAccptdInstdBal.deleter
	def OptnAccptdInstdBal(self):
		del self._OptnAccptdInstdBal
		self._OptnAccptdInstdBal = None

	@property
	def OptnPdgInstrBal(self):
		return self._OptnPdgInstrBal

	@OptnPdgInstrBal.setter
	def OptnPdgInstrBal(self, value):
		self._OptnPdgInstrBal = value if type(value) != auto else self.make_default("OptnPdgInstrBal")

	@OptnPdgInstrBal.deleter
	def OptnPdgInstrBal(self):
		del self._OptnPdgInstrBal
		self._OptnPdgInstrBal = None

	@property
	def OptnRtrdInstdBal(self):
		return self._OptnRtrdInstdBal

	@OptnRtrdInstdBal.setter
	def OptnRtrdInstdBal(self, value):
		self._OptnRtrdInstdBal = value if type(value) != auto else self.make_default("OptnRtrdInstdBal")

	@OptnRtrdInstdBal.deleter
	def OptnRtrdInstdBal(self):
		del self._OptnRtrdInstdBal
		self._OptnRtrdInstdBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltActn', type=DefaultProcessingOrStandingInstruction2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=BalanceFormat14Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption36Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnCancInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnRjctdInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPrtctInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDdlns', type=CorporateActionEventDeadlines4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnInstrDtls', type=OptionInstructionDetails12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnAccptdInstdBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPdgInstrBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnRtrdInstdBal', type=SignedQuantityFormat16, min=0, max=1, mutex_group=None, array=False),
	))

