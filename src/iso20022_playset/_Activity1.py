# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max70Text

class Activity1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_MsgNm"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if value is not None else base_types.UninitialisedField(self, 'MsgNm', Max70Text, False)

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = base_types.UninitialisedField(self, 'MsgNm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
	))