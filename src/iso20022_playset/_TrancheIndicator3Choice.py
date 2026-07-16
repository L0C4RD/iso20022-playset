# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import Tranche3

class TrancheIndicator3Choice(base_types._BaseFieldType):

	__slots__ = ["_Trnchd", "_Utrnchd"]
	@property
	def Trnchd(self):
		return self._Trnchd

	@Trnchd.setter
	def Trnchd(self, value):
		self._Trnchd = value if value is not None else base_types.UninitialisedField(self, 'Trnchd', Tranche3, False)

	@Trnchd.deleter
	def Trnchd(self):
		del self._Trnchd
		self._Trnchd = base_types.UninitialisedField(self, 'Trnchd', Tranche3, False)

	@property
	def Utrnchd(self):
		return self._Utrnchd

	@Utrnchd.setter
	def Utrnchd(self, value):
		self._Utrnchd = value if value is not None else base_types.UninitialisedField(self, 'Utrnchd', NoReasonCode, False)

	@Utrnchd.deleter
	def Utrnchd(self):
		del self._Utrnchd
		self._Utrnchd = base_types.UninitialisedField(self, 'Utrnchd', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trnchd', type=Tranche3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Utrnchd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))