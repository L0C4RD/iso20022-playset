# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReservationIdentification4
from . import ReservationOrError9Choice

class ReservationReport8(base_types._BaseFieldType):

	__slots__ = ["_RsvatnId", "_RsvatnOrErr"]
	@property
	def RsvatnId(self):
		return self._RsvatnId

	@RsvatnId.setter
	def RsvatnId(self, value):
		self._RsvatnId = value if value is not None else base_types.UninitialisedField(self, 'RsvatnId', ReservationIdentification4, False)

	@RsvatnId.deleter
	def RsvatnId(self):
		del self._RsvatnId
		self._RsvatnId = base_types.UninitialisedField(self, 'RsvatnId', ReservationIdentification4, False)

	@property
	def RsvatnOrErr(self):
		return self._RsvatnOrErr

	@RsvatnOrErr.setter
	def RsvatnOrErr(self, value):
		self._RsvatnOrErr = value if value is not None else base_types.UninitialisedField(self, 'RsvatnOrErr', ReservationOrError9Choice, False)

	@RsvatnOrErr.deleter
	def RsvatnOrErr(self):
		del self._RsvatnOrErr
		self._RsvatnOrErr = base_types.UninitialisedField(self, 'RsvatnOrErr', ReservationOrError9Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsvatnId', type=ReservationIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnOrErr', type=ReservationOrError9Choice, min=1, max=1, mutex_group=None, array=False),
	))