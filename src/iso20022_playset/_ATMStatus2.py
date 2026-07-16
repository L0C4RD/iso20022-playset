# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMStatus1Code
from . import Max35Text

class ATMStatus2(base_types._BaseFieldType):

	__slots__ = ["_CurSts", "_CurStsRsn", "_DmnddSts"]
	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if value is not None else base_types.UninitialisedField(self, 'CurSts', ATMStatus1Code, False)

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = base_types.UninitialisedField(self, 'CurSts', ATMStatus1Code, False)

	@property
	def CurStsRsn(self):
		return self._CurStsRsn

	@CurStsRsn.setter
	def CurStsRsn(self, value):
		self._CurStsRsn = value if value is not None else base_types.UninitialisedField(self, 'CurStsRsn', Max35Text, True)

	@CurStsRsn.deleter
	def CurStsRsn(self):
		del self._CurStsRsn
		self._CurStsRsn = base_types.UninitialisedField(self, 'CurStsRsn', Max35Text, True)

	@property
	def DmnddSts(self):
		return self._DmnddSts

	@DmnddSts.setter
	def DmnddSts(self, value):
		self._DmnddSts = value if value is not None else base_types.UninitialisedField(self, 'DmnddSts', ATMStatus1Code, False)

	@DmnddSts.deleter
	def DmnddSts(self):
		del self._DmnddSts
		self._DmnddSts = base_types.UninitialisedField(self, 'DmnddSts', ATMStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurSts', type=ATMStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DmnddSts', type=ATMStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))