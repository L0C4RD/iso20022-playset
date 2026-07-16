# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeData43

class TradeReport33Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmprssn", "_Crrctn", "_Err", "_Mod", "_New", "_Othr", "_PortOut", "_PosCmpnt", "_Rvv", "_Termntn", "_ValtnUpd"]
	@property
	def Cmprssn(self):
		return self._Cmprssn

	@Cmprssn.setter
	def Cmprssn(self, value):
		self._Cmprssn = value if value is not None else base_types.UninitialisedField(self, 'Cmprssn', TradeData43, False)

	@Cmprssn.deleter
	def Cmprssn(self):
		del self._Cmprssn
		self._Cmprssn = base_types.UninitialisedField(self, 'Cmprssn', TradeData43, False)

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if value is not None else base_types.UninitialisedField(self, 'Crrctn', TradeData43, False)

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = base_types.UninitialisedField(self, 'Crrctn', TradeData43, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', TradeData43, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', TradeData43, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', TradeData43, False)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', TradeData43, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', TradeData43, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', TradeData43, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', TradeData43, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', TradeData43, False)

	@property
	def PortOut(self):
		return self._PortOut

	@PortOut.setter
	def PortOut(self, value):
		self._PortOut = value if value is not None else base_types.UninitialisedField(self, 'PortOut', TradeData43, False)

	@PortOut.deleter
	def PortOut(self):
		del self._PortOut
		self._PortOut = base_types.UninitialisedField(self, 'PortOut', TradeData43, False)

	@property
	def PosCmpnt(self):
		return self._PosCmpnt

	@PosCmpnt.setter
	def PosCmpnt(self, value):
		self._PosCmpnt = value if value is not None else base_types.UninitialisedField(self, 'PosCmpnt', TradeData43, False)

	@PosCmpnt.deleter
	def PosCmpnt(self):
		del self._PosCmpnt
		self._PosCmpnt = base_types.UninitialisedField(self, 'PosCmpnt', TradeData43, False)

	@property
	def Rvv(self):
		return self._Rvv

	@Rvv.setter
	def Rvv(self, value):
		self._Rvv = value if value is not None else base_types.UninitialisedField(self, 'Rvv', TradeData43, False)

	@Rvv.deleter
	def Rvv(self):
		del self._Rvv
		self._Rvv = base_types.UninitialisedField(self, 'Rvv', TradeData43, False)

	@property
	def Termntn(self):
		return self._Termntn

	@Termntn.setter
	def Termntn(self, value):
		self._Termntn = value if value is not None else base_types.UninitialisedField(self, 'Termntn', TradeData43, False)

	@Termntn.deleter
	def Termntn(self):
		del self._Termntn
		self._Termntn = base_types.UninitialisedField(self, 'Termntn', TradeData43, False)

	@property
	def ValtnUpd(self):
		return self._ValtnUpd

	@ValtnUpd.setter
	def ValtnUpd(self, value):
		self._ValtnUpd = value if value is not None else base_types.UninitialisedField(self, 'ValtnUpd', TradeData43, False)

	@ValtnUpd.deleter
	def ValtnUpd(self):
		del self._ValtnUpd
		self._ValtnUpd = base_types.UninitialisedField(self, 'ValtnUpd', TradeData43, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmprssn', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PortOut', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PosCmpnt', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rvv', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Termntn', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValtnUpd', type=TradeData43, min=0, max=1, mutex_group=1, array=False),
	))