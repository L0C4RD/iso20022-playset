import base_types
import ProprietaryStatusAndReason6
import ProprietaryReason4

class ReplacementProcessingStatus10Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtlRplcmntAccptd", "_Dnd", "_Pdg", "_RcvdAtStockXchg", "_Rjctd", "_Cmpltd", "_ModReqd", "_Accptd", "_InRpr", "_PrtrySts", "_RcvdAtIntrmy"]
	@property
	def PrtlRplcmntAccptd(self):
		return self._PrtlRplcmntAccptd

	@PrtlRplcmntAccptd.setter
	def PrtlRplcmntAccptd(self, value):
		self._PrtlRplcmntAccptd = value if type(value) != auto else self.make_default("PrtlRplcmntAccptd")

	@PrtlRplcmntAccptd.deleter
	def PrtlRplcmntAccptd(self):
		del self._PrtlRplcmntAccptd
		self._PrtlRplcmntAccptd = None

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if type(value) != auto else self.make_default("Dnd")

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def RcvdAtStockXchg(self):
		return self._RcvdAtStockXchg

	@RcvdAtStockXchg.setter
	def RcvdAtStockXchg(self, value):
		self._RcvdAtStockXchg = value if type(value) != auto else self.make_default("RcvdAtStockXchg")

	@RcvdAtStockXchg.deleter
	def RcvdAtStockXchg(self):
		del self._RcvdAtStockXchg
		self._RcvdAtStockXchg = None

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
	def Cmpltd(self):
		return self._Cmpltd

	@Cmpltd.setter
	def Cmpltd(self, value):
		self._Cmpltd = value if type(value) != auto else self.make_default("Cmpltd")

	@Cmpltd.deleter
	def Cmpltd(self):
		del self._Cmpltd
		self._Cmpltd = None

	@property
	def ModReqd(self):
		return self._ModReqd

	@ModReqd.setter
	def ModReqd(self, value):
		self._ModReqd = value if type(value) != auto else self.make_default("ModReqd")

	@ModReqd.deleter
	def ModReqd(self):
		del self._ModReqd
		self._ModReqd = None

	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

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
	def RcvdAtIntrmy(self):
		return self._RcvdAtIntrmy

	@RcvdAtIntrmy.setter
	def RcvdAtIntrmy(self, value):
		self._RcvdAtIntrmy = value if type(value) != auto else self.make_default("RcvdAtIntrmy")

	@RcvdAtIntrmy.deleter
	def RcvdAtIntrmy(self):
		del self._RcvdAtIntrmy
		self._RcvdAtIntrmy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtlRplcmntAccptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdAtStockXchg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmpltd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Accptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InRpr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdAtIntrmy', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))

