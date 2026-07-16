# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max4000Text
from . import Max500Text
from . import MessageError1Code

class ErrorDetails3(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_DataElmtInErr", "_Desc", "_OthrTp", "_Tp"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@property
	def DataElmtInErr(self):
		return self._DataElmtInErr

	@DataElmtInErr.setter
	def DataElmtInErr(self, value):
		self._DataElmtInErr = value if value is not None else base_types.UninitialisedField(self, 'DataElmtInErr', Max4000Text, True)

	@DataElmtInErr.deleter
	def DataElmtInErr(self):
		del self._DataElmtInErr
		self._DataElmtInErr = base_types.UninitialisedField(self, 'DataElmtInErr', Max4000Text, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max500Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max500Text, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MessageError1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MessageError1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataElmtInErr', type=Max4000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MessageError1Code, min=1, max=1, mutex_group=None, array=False),
	))