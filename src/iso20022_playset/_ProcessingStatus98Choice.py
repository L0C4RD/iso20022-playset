# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstructionProcessingReason3Choice
from . import InstructionProcessingReason4Choice
from . import PendingProcessing2Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class ProcessingStatus98Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_AlrdyMtchdAndAffrmd", "_DfltActn", "_Done", "_ForcdRjctn", "_FullyExctdConfSnt", "_Futr", "_Gnrtd", "_InRpr", "_NoInstr", "_OpnOrdr", "_PdgPrcg", "_PrtrySts", "_RcvdAtIntrmy", "_Rjctd", "_StgInstr", "_SttlmInstrSnt", "_TradgSspdByStockXchg", "_Trtd"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptd', ProprietaryReason4, False)

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = base_types.UninitialisedField(self, 'AckdAccptd', ProprietaryReason4, False)

	@property
	def AlrdyMtchdAndAffrmd(self):
		return self._AlrdyMtchdAndAffrmd

	@AlrdyMtchdAndAffrmd.setter
	def AlrdyMtchdAndAffrmd(self, value):
		self._AlrdyMtchdAndAffrmd = value if value is not None else base_types.UninitialisedField(self, 'AlrdyMtchdAndAffrmd', ProprietaryReason4, False)

	@AlrdyMtchdAndAffrmd.deleter
	def AlrdyMtchdAndAffrmd(self):
		del self._AlrdyMtchdAndAffrmd
		self._AlrdyMtchdAndAffrmd = base_types.UninitialisedField(self, 'AlrdyMtchdAndAffrmd', ProprietaryReason4, False)

	@property
	def DfltActn(self):
		return self._DfltActn

	@DfltActn.setter
	def DfltActn(self, value):
		self._DfltActn = value if value is not None else base_types.UninitialisedField(self, 'DfltActn', ProprietaryReason4, False)

	@DfltActn.deleter
	def DfltActn(self):
		del self._DfltActn
		self._DfltActn = base_types.UninitialisedField(self, 'DfltActn', ProprietaryReason4, False)

	@property
	def Done(self):
		return self._Done

	@Done.setter
	def Done(self, value):
		self._Done = value if value is not None else base_types.UninitialisedField(self, 'Done', ProprietaryReason4, False)

	@Done.deleter
	def Done(self):
		del self._Done
		self._Done = base_types.UninitialisedField(self, 'Done', ProprietaryReason4, False)

	@property
	def ForcdRjctn(self):
		return self._ForcdRjctn

	@ForcdRjctn.setter
	def ForcdRjctn(self, value):
		self._ForcdRjctn = value if value is not None else base_types.UninitialisedField(self, 'ForcdRjctn', ProprietaryReason4, False)

	@ForcdRjctn.deleter
	def ForcdRjctn(self):
		del self._ForcdRjctn
		self._ForcdRjctn = base_types.UninitialisedField(self, 'ForcdRjctn', ProprietaryReason4, False)

	@property
	def FullyExctdConfSnt(self):
		return self._FullyExctdConfSnt

	@FullyExctdConfSnt.setter
	def FullyExctdConfSnt(self, value):
		self._FullyExctdConfSnt = value if value is not None else base_types.UninitialisedField(self, 'FullyExctdConfSnt', ProprietaryReason4, False)

	@FullyExctdConfSnt.deleter
	def FullyExctdConfSnt(self):
		del self._FullyExctdConfSnt
		self._FullyExctdConfSnt = base_types.UninitialisedField(self, 'FullyExctdConfSnt', ProprietaryReason4, False)

	@property
	def Futr(self):
		return self._Futr

	@Futr.setter
	def Futr(self, value):
		self._Futr = value if value is not None else base_types.UninitialisedField(self, 'Futr', ProprietaryReason4, False)

	@Futr.deleter
	def Futr(self):
		del self._Futr
		self._Futr = base_types.UninitialisedField(self, 'Futr', ProprietaryReason4, False)

	@property
	def Gnrtd(self):
		return self._Gnrtd

	@Gnrtd.setter
	def Gnrtd(self, value):
		self._Gnrtd = value if value is not None else base_types.UninitialisedField(self, 'Gnrtd', ProprietaryReason4, False)

	@Gnrtd.deleter
	def Gnrtd(self):
		del self._Gnrtd
		self._Gnrtd = base_types.UninitialisedField(self, 'Gnrtd', ProprietaryReason4, False)

	@property
	def InRpr(self):
		return self._InRpr

	@InRpr.setter
	def InRpr(self, value):
		self._InRpr = value if value is not None else base_types.UninitialisedField(self, 'InRpr', InstructionProcessingReason4Choice, False)

	@InRpr.deleter
	def InRpr(self):
		del self._InRpr
		self._InRpr = base_types.UninitialisedField(self, 'InRpr', InstructionProcessingReason4Choice, False)

	@property
	def NoInstr(self):
		return self._NoInstr

	@NoInstr.setter
	def NoInstr(self, value):
		self._NoInstr = value if value is not None else base_types.UninitialisedField(self, 'NoInstr', ProprietaryReason4, False)

	@NoInstr.deleter
	def NoInstr(self):
		del self._NoInstr
		self._NoInstr = base_types.UninitialisedField(self, 'NoInstr', ProprietaryReason4, False)

	@property
	def OpnOrdr(self):
		return self._OpnOrdr

	@OpnOrdr.setter
	def OpnOrdr(self, value):
		self._OpnOrdr = value if value is not None else base_types.UninitialisedField(self, 'OpnOrdr', ProprietaryReason4, False)

	@OpnOrdr.deleter
	def OpnOrdr(self):
		del self._OpnOrdr
		self._OpnOrdr = base_types.UninitialisedField(self, 'OpnOrdr', ProprietaryReason4, False)

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessing2Choice, False)

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessing2Choice, False)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@property
	def RcvdAtIntrmy(self):
		return self._RcvdAtIntrmy

	@RcvdAtIntrmy.setter
	def RcvdAtIntrmy(self, value):
		self._RcvdAtIntrmy = value if value is not None else base_types.UninitialisedField(self, 'RcvdAtIntrmy', ProprietaryReason4, False)

	@RcvdAtIntrmy.deleter
	def RcvdAtIntrmy(self):
		del self._RcvdAtIntrmy
		self._RcvdAtIntrmy = base_types.UninitialisedField(self, 'RcvdAtIntrmy', ProprietaryReason4, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', InstructionProcessingReason3Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', InstructionProcessingReason3Choice, False)

	@property
	def StgInstr(self):
		return self._StgInstr

	@StgInstr.setter
	def StgInstr(self, value):
		self._StgInstr = value if value is not None else base_types.UninitialisedField(self, 'StgInstr', ProprietaryReason4, False)

	@StgInstr.deleter
	def StgInstr(self):
		del self._StgInstr
		self._StgInstr = base_types.UninitialisedField(self, 'StgInstr', ProprietaryReason4, False)

	@property
	def SttlmInstrSnt(self):
		return self._SttlmInstrSnt

	@SttlmInstrSnt.setter
	def SttlmInstrSnt(self, value):
		self._SttlmInstrSnt = value if value is not None else base_types.UninitialisedField(self, 'SttlmInstrSnt', ProprietaryReason4, False)

	@SttlmInstrSnt.deleter
	def SttlmInstrSnt(self):
		del self._SttlmInstrSnt
		self._SttlmInstrSnt = base_types.UninitialisedField(self, 'SttlmInstrSnt', ProprietaryReason4, False)

	@property
	def TradgSspdByStockXchg(self):
		return self._TradgSspdByStockXchg

	@TradgSspdByStockXchg.setter
	def TradgSspdByStockXchg(self, value):
		self._TradgSspdByStockXchg = value if value is not None else base_types.UninitialisedField(self, 'TradgSspdByStockXchg', ProprietaryReason4, False)

	@TradgSspdByStockXchg.deleter
	def TradgSspdByStockXchg(self):
		del self._TradgSspdByStockXchg
		self._TradgSspdByStockXchg = base_types.UninitialisedField(self, 'TradgSspdByStockXchg', ProprietaryReason4, False)

	@property
	def Trtd(self):
		return self._Trtd

	@Trtd.setter
	def Trtd(self, value):
		self._Trtd = value if value is not None else base_types.UninitialisedField(self, 'Trtd', ProprietaryReason4, False)

	@Trtd.deleter
	def Trtd(self):
		del self._Trtd
		self._Trtd = base_types.UninitialisedField(self, 'Trtd', ProprietaryReason4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AlrdyMtchdAndAffrmd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DfltActn', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Done', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ForcdRjctn', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FullyExctdConfSnt', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Futr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gnrtd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InRpr', type=InstructionProcessingReason4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoInstr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OpnOrdr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessing2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdAtIntrmy', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=InstructionProcessingReason3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmInstrSnt', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TradgSspdByStockXchg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trtd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))