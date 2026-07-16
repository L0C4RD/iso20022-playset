# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class OrganisationIdentification5(base_types._BaseFieldType):

	__slots__ = ["_RegnNb", "_RegrNm"]
	@property
	def RegnNb(self):
		return self._RegnNb

	@RegnNb.setter
	def RegnNb(self, value):
		self._RegnNb = value if value is not None else base_types.UninitialisedField(self, 'RegnNb', Max35Text, False)

	@RegnNb.deleter
	def RegnNb(self):
		del self._RegnNb
		self._RegnNb = base_types.UninitialisedField(self, 'RegnNb', Max35Text, False)

	@property
	def RegrNm(self):
		return self._RegrNm

	@RegrNm.setter
	def RegrNm(self, value):
		self._RegrNm = value if value is not None else base_types.UninitialisedField(self, 'RegrNm', Max35Text, False)

	@RegrNm.deleter
	def RegrNm(self):
		del self._RegrNm
		self._RegrNm = base_types.UninitialisedField(self, 'RegrNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))