# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndividualPerson29
from . import Organisation23

class RegisteredShareholderName1Choice(base_types._BaseFieldType):

	__slots__ = ["_IndvPrsn", "_Org"]
	@property
	def IndvPrsn(self):
		return self._IndvPrsn

	@IndvPrsn.setter
	def IndvPrsn(self, value):
		self._IndvPrsn = value if value is not None else base_types.UninitialisedField(self, 'IndvPrsn', IndividualPerson29, False)

	@IndvPrsn.deleter
	def IndvPrsn(self):
		del self._IndvPrsn
		self._IndvPrsn = base_types.UninitialisedField(self, 'IndvPrsn', IndividualPerson29, False)

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if value is not None else base_types.UninitialisedField(self, 'Org', Organisation23, False)

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = base_types.UninitialisedField(self, 'Org', Organisation23, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvPrsn', type=IndividualPerson29, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Org', type=Organisation23, min=0, max=1, mutex_group=1, array=False),
	))