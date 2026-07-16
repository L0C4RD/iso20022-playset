# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Direction2
from . import OptionParty1Code

class Direction4Choice(base_types._BaseFieldType):

	__slots__ = ["_CtrPtySd", "_Drctn"]
	@property
	def CtrPtySd(self):
		return self._CtrPtySd

	@CtrPtySd.setter
	def CtrPtySd(self, value):
		self._CtrPtySd = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySd', OptionParty1Code, False)

	@CtrPtySd.deleter
	def CtrPtySd(self):
		del self._CtrPtySd
		self._CtrPtySd = base_types.UninitialisedField(self, 'CtrPtySd', OptionParty1Code, False)

	@property
	def Drctn(self):
		return self._Drctn

	@Drctn.setter
	def Drctn(self, value):
		self._Drctn = value if value is not None else base_types.UninitialisedField(self, 'Drctn', Direction2, False)

	@Drctn.deleter
	def Drctn(self):
		del self._Drctn
		self._Drctn = base_types.UninitialisedField(self, 'Drctn', Direction2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtySd', type=OptionParty1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Drctn', type=Direction2, min=0, max=1, mutex_group=1, array=False),
	))