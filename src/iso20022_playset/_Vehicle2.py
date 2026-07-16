# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading5Code
from . import Max35Text

class Vehicle2(base_types._BaseFieldType):

	__slots__ = ["_Data", "_NtryMd", "_Tp"]
	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', Max35Text, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', Max35Text, False)

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if value is not None else base_types.UninitialisedField(self, 'NtryMd', CardDataReading5Code, False)

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = base_types.UninitialisedField(self, 'NtryMd', CardDataReading5Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Data', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))