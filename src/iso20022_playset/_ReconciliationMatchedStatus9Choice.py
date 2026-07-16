# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import ReconciliationResult10

class ReconciliationMatchedStatus9Choice(base_types._BaseFieldType):

	__slots__ = ["_Mtchd", "_NotMtchd"]
	@property
	def Mtchd(self):
		return self._Mtchd

	@Mtchd.setter
	def Mtchd(self, value):
		self._Mtchd = value if value is not None else base_types.UninitialisedField(self, 'Mtchd', NoReasonCode, False)

	@Mtchd.deleter
	def Mtchd(self):
		del self._Mtchd
		self._Mtchd = base_types.UninitialisedField(self, 'Mtchd', NoReasonCode, False)

	@property
	def NotMtchd(self):
		return self._NotMtchd

	@NotMtchd.setter
	def NotMtchd(self, value):
		self._NotMtchd = value if value is not None else base_types.UninitialisedField(self, 'NotMtchd', ReconciliationResult10, False)

	@NotMtchd.deleter
	def NotMtchd(self):
		del self._NotMtchd
		self._NotMtchd = base_types.UninitialisedField(self, 'NotMtchd', ReconciliationResult10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtchd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotMtchd', type=ReconciliationResult10, min=0, max=1, mutex_group=1, array=False),
	))