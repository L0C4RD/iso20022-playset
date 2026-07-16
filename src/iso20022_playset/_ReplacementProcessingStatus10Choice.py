# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class ReplacementProcessingStatus10Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_Cmpltd", "_Dnd", "_InRpr", "_ModReqd", "_Pdg", "_PrtlRplcmntAccptd", "_PrtrySts", "_RcvdAtIntrmy", "_RcvdAtStockXchg", "_Rjctd"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if value is not None else base_types.UninitialisedField(self, 'Accptd', ProprietaryReason4, False)

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = base_types.UninitialisedField(self, 'Accptd', ProprietaryReason4, False)

	@property
	def Cmpltd(self):
		return self._Cmpltd

	@Cmpltd.setter
	def Cmpltd(self, value):
		self._Cmpltd = value if value is not None else base_types.UninitialisedField(self, 'Cmpltd', ProprietaryReason4, False)

	@Cmpltd.deleter
	def Cmpltd(self):
		del self._Cmpltd
		self._Cmpltd = base_types.UninitialisedField(self, 'Cmpltd', ProprietaryReason4, False)

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if value is not None else base_types.UninitialisedField(self, 'Dnd', ProprietaryReason4, False)

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = base_types.UninitialisedField(self, 'Dnd', ProprietaryReason4, False)

	@property
	def InRpr(self):
		return self._InRpr

	@InRpr.setter
	def InRpr(self, value):
		self._InRpr = value if value is not None else base_types.UninitialisedField(self, 'InRpr', ProprietaryReason4, False)

	@InRpr.deleter
	def InRpr(self):
		del self._InRpr
		self._InRpr = base_types.UninitialisedField(self, 'InRpr', ProprietaryReason4, False)

	@property
	def ModReqd(self):
		return self._ModReqd

	@ModReqd.setter
	def ModReqd(self, value):
		self._ModReqd = value if value is not None else base_types.UninitialisedField(self, 'ModReqd', ProprietaryReason4, False)

	@ModReqd.deleter
	def ModReqd(self):
		del self._ModReqd
		self._ModReqd = base_types.UninitialisedField(self, 'ModReqd', ProprietaryReason4, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', ProprietaryReason4, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', ProprietaryReason4, False)

	@property
	def PrtlRplcmntAccptd(self):
		return self._PrtlRplcmntAccptd

	@PrtlRplcmntAccptd.setter
	def PrtlRplcmntAccptd(self, value):
		self._PrtlRplcmntAccptd = value if value is not None else base_types.UninitialisedField(self, 'PrtlRplcmntAccptd', ProprietaryReason4, False)

	@PrtlRplcmntAccptd.deleter
	def PrtlRplcmntAccptd(self):
		del self._PrtlRplcmntAccptd
		self._PrtlRplcmntAccptd = base_types.UninitialisedField(self, 'PrtlRplcmntAccptd', ProprietaryReason4, False)

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
	def RcvdAtStockXchg(self):
		return self._RcvdAtStockXchg

	@RcvdAtStockXchg.setter
	def RcvdAtStockXchg(self, value):
		self._RcvdAtStockXchg = value if value is not None else base_types.UninitialisedField(self, 'RcvdAtStockXchg', ProprietaryReason4, False)

	@RcvdAtStockXchg.deleter
	def RcvdAtStockXchg(self):
		del self._RcvdAtStockXchg
		self._RcvdAtStockXchg = base_types.UninitialisedField(self, 'RcvdAtStockXchg', ProprietaryReason4, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', ProprietaryReason4, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', ProprietaryReason4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmpltd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InRpr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtlRplcmntAccptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdAtIntrmy', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcvdAtStockXchg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))