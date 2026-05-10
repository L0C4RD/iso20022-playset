from . import base_types
from ._Direction2 import Direction2
from ._OptionParty1Code import OptionParty1Code

class Direction4Choice(base_types._BaseFieldType):

	__slots__ = ["_Drctn", "_CtrPtySd"]
	@property
	def CtrPtySd(self):
		return self._CtrPtySd

	@CtrPtySd.setter
	def CtrPtySd(self, value):
		self._CtrPtySd = value if type(value) != base_types.auto else self.make_default("CtrPtySd")

	@CtrPtySd.deleter
	def CtrPtySd(self):
		del self._CtrPtySd
		self._CtrPtySd = None

	@property
	def Drctn(self):
		return self._Drctn

	@Drctn.setter
	def Drctn(self, value):
		self._Drctn = value if type(value) != base_types.auto else self.make_default("Drctn")

	@Drctn.deleter
	def Drctn(self):
		del self._Drctn
		self._Drctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtySd', type=OptionParty1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Drctn', type=Direction2, min=0, max=1, mutex_group=1, array=False),
	))

