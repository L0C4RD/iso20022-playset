import base_types
import InstructionProcessingReason3Choice
import PendingProcessing2Choice
import InstructionProcessingReason4Choice
import ProprietaryStatusAndReason6
import ProprietaryReason4

class ProcessingStatus98Choice(base_types._BaseFieldType):

	__slots__ = ["_FullyExctdConfSnt", "_StgInstr", "_Trtd", "_ForcdRjctn", "_Done", "_OpnOrdr", "_PrtrySts", "_NoInstr", "_Futr", "_DfltActn", "_TradgSspdByStockXchg", "_Rjctd", "_AckdAccptd", "_InRpr", "_PdgPrcg", "_RcvdAtIntrmy", "_AlrdyMtchdAndAffrmd", "_Gnrtd", "_SttlmInstrSnt"]
	@property
	def FullyExctdConfSnt(self):
		return self._FullyExctdConfSnt

	@FullyExctdConfSnt.setter
	def FullyExctdConfSnt(self, value):
		self._FullyExctdConfSnt = value if type(value) != auto else self.make_default("FullyExctdConfSnt")

	@FullyExctdConfSnt.deleter
	def FullyExctdConfSnt(self):
		del self._FullyExctdConfSnt
		self._FullyExctdConfSnt = None

	@property
	def StgInstr(self):
		return self._StgInstr

	@StgInstr.setter
	def StgInstr(self, value):
		self._StgInstr = value if type(value) != auto else self.make_default("StgInstr")

	@StgInstr.deleter
	def StgInstr(self):
		del self._StgInstr
		self._StgInstr = None

	@property
	def Trtd(self):
		return self._Trtd

	@Trtd.setter
	def Trtd(self, value):
		self._Trtd = value if type(value) != auto else self.make_default("Trtd")

	@Trtd.deleter
	def Trtd(self):
		del self._Trtd
		self._Trtd = None

	@property
	def ForcdRjctn(self):
		return self._ForcdRjctn

	@ForcdRjctn.setter
	def ForcdRjctn(self, value):
		self._ForcdRjctn = value if type(value) != auto else self.make_default("ForcdRjctn")

	@ForcdRjctn.deleter
	def ForcdRjctn(self):
		del self._ForcdRjctn
		self._ForcdRjctn = None

	@property
	def Done(self):
		return self._Done

	@Done.setter
	def Done(self, value):
		self._Done = value if type(value) != auto else self.make_default("Done")

	@Done.deleter
	def Done(self):
		del self._Done
		self._Done = None

	@property
	def OpnOrdr(self):
		return self._OpnOrdr

	@OpnOrdr.setter
	def OpnOrdr(self, value):
		self._OpnOrdr = value if type(value) != auto else self.make_default("OpnOrdr")

	@OpnOrdr.deleter
	def OpnOrdr(self):
		del self._OpnOrdr
		self._OpnOrdr = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	@property
	def NoInstr(self):
		return self._NoInstr

	@NoInstr.setter
	def NoInstr(self, value):
		self._NoInstr = value if type(value) != auto else self.make_default("NoInstr")

	@NoInstr.deleter
	def NoInstr(self):
		del self._NoInstr
		self._NoInstr = None

	@property
	def Futr(self):
		return self._Futr

	@Futr.setter
	def Futr(self, value):
		self._Futr = value if type(value) != auto else self.make_default("Futr")

	@Futr.deleter
	def Futr(self):
		del self._Futr
		self._Futr = None

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
	def TradgSspdByStockXchg(self):
		return self._TradgSspdByStockXchg

	@TradgSspdByStockXchg.setter
	def TradgSspdByStockXchg(self, value):
		self._TradgSspdByStockXchg = value if type(value) != auto else self.make_default("TradgSspdByStockXchg")

	@TradgSspdByStockXchg.deleter
	def TradgSspdByStockXchg(self):
		del self._TradgSspdByStockXchg
		self._TradgSspdByStockXchg = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	@property
	def InRpr(self):
		return self._InRpr

	@InRpr.setter
	def InRpr(self, value):
		self._InRpr = value if type(value) != auto else self.make_default("InRpr")

	@InRpr.deleter
	def InRpr(self):
		del self._InRpr
		self._InRpr = None

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if type(value) != auto else self.make_default("PdgPrcg")

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = None

	@property
	def RcvdAtIntrmy(self):
		return self._RcvdAtIntrmy

	@RcvdAtIntrmy.setter
	def RcvdAtIntrmy(self, value):
		self._RcvdAtIntrmy = value if type(value) != auto else self.make_default("RcvdAtIntrmy")

	@RcvdAtIntrmy.deleter
	def RcvdAtIntrmy(self):
		del self._RcvdAtIntrmy
		self._RcvdAtIntrmy = None

	@property
	def AlrdyMtchdAndAffrmd(self):
		return self._AlrdyMtchdAndAffrmd

	@AlrdyMtchdAndAffrmd.setter
	def AlrdyMtchdAndAffrmd(self, value):
		self._AlrdyMtchdAndAffrmd = value if type(value) != auto else self.make_default("AlrdyMtchdAndAffrmd")

	@AlrdyMtchdAndAffrmd.deleter
	def AlrdyMtchdAndAffrmd(self):
		del self._AlrdyMtchdAndAffrmd
		self._AlrdyMtchdAndAffrmd = None

	@property
	def Gnrtd(self):
		return self._Gnrtd

	@Gnrtd.setter
	def Gnrtd(self, value):
		self._Gnrtd = value if type(value) != auto else self.make_default("Gnrtd")

	@Gnrtd.deleter
	def Gnrtd(self):
		del self._Gnrtd
		self._Gnrtd = None

	@property
	def SttlmInstrSnt(self):
		return self._SttlmInstrSnt

	@SttlmInstrSnt.setter
	def SttlmInstrSnt(self, value):
		self._SttlmInstrSnt = value if type(value) != auto else self.make_default("SttlmInstrSnt")

	@SttlmInstrSnt.deleter
	def SttlmInstrSnt(self):
		del self._SttlmInstrSnt
		self._SttlmInstrSnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullyExctdConfSnt', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trtd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ForcdRjctn', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Done', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OpnOrdr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoInstr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Futr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DfltActn', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TradgSspdByStockXchg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=InstructionProcessingReason3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InRpr', type=InstructionProcessingReason4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessing2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdAtIntrmy', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AlrdyMtchdAndAffrmd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gnrtd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmInstrSnt', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))

