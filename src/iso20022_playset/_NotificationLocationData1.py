# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationLocationMethod1Code
from . import Max2048Text
from . import NameAndAddress18

class NotificationLocationData1(base_types._BaseFieldType):

	__slots__ = ["_ElctrncAdr", "_Mtd", "_PstlAdr"]
	@property
	def ElctrncAdr(self):
		return self._ElctrncAdr

	@ElctrncAdr.setter
	def ElctrncAdr(self, value):
		self._ElctrncAdr = value if value is not None else base_types.UninitialisedField(self, 'ElctrncAdr', Max2048Text, False)

	@ElctrncAdr.deleter
	def ElctrncAdr(self):
		del self._ElctrncAdr
		self._ElctrncAdr = base_types.UninitialisedField(self, 'ElctrncAdr', Max2048Text, False)

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if value is not None else base_types.UninitialisedField(self, 'Mtd', InvestigationLocationMethod1Code, False)

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = base_types.UninitialisedField(self, 'Mtd', InvestigationLocationMethod1Code, False)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', NameAndAddress18, False)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', NameAndAddress18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=InvestigationLocationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
	))