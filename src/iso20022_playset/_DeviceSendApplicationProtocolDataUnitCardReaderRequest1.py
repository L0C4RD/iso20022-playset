# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Min1Max256Binary

class DeviceSendApplicationProtocolDataUnitCardReaderRequest1(base_types._BaseFieldType):

	__slots__ = ["_Clss", "_Data", "_Instr", "_Param1", "_Param2", "_XpctdLngth"]
	@property
	def Clss(self):
		return self._Clss

	@Clss.setter
	def Clss(self, value):
		self._Clss = value if value is not None else base_types.UninitialisedField(self, 'Clss', Min1Max256Binary, False)

	@Clss.deleter
	def Clss(self):
		del self._Clss
		self._Clss = base_types.UninitialisedField(self, 'Clss', Min1Max256Binary, False)

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', Min1Max256Binary, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', Min1Max256Binary, False)

	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if value is not None else base_types.UninitialisedField(self, 'Instr', Min1Max256Binary, False)

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = base_types.UninitialisedField(self, 'Instr', Min1Max256Binary, False)

	@property
	def Param1(self):
		return self._Param1

	@Param1.setter
	def Param1(self, value):
		self._Param1 = value if value is not None else base_types.UninitialisedField(self, 'Param1', Min1Max256Binary, False)

	@Param1.deleter
	def Param1(self):
		del self._Param1
		self._Param1 = base_types.UninitialisedField(self, 'Param1', Min1Max256Binary, False)

	@property
	def Param2(self):
		return self._Param2

	@Param2.setter
	def Param2(self, value):
		self._Param2 = value if value is not None else base_types.UninitialisedField(self, 'Param2', Min1Max256Binary, False)

	@Param2.deleter
	def Param2(self):
		del self._Param2
		self._Param2 = base_types.UninitialisedField(self, 'Param2', Min1Max256Binary, False)

	@property
	def XpctdLngth(self):
		return self._XpctdLngth

	@XpctdLngth.setter
	def XpctdLngth(self, value):
		self._XpctdLngth = value if value is not None else base_types.UninitialisedField(self, 'XpctdLngth', Min1Max256Binary, False)

	@XpctdLngth.deleter
	def XpctdLngth(self):
		del self._XpctdLngth
		self._XpctdLngth = base_types.UninitialisedField(self, 'XpctdLngth', Min1Max256Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clss', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=Min1Max256Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instr', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param1', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param2', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdLngth', type=Min1Max256Binary, min=0, max=1, mutex_group=None, array=False),
	))