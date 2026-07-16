# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardSecurityCapability1Code
from . import Max35Text

class CardSecurityCapability1(base_types._BaseFieldType):

	__slots__ = ["_Cpblty", "_OthrCpblty"]
	@property
	def Cpblty(self):
		return self._Cpblty

	@Cpblty.setter
	def Cpblty(self, value):
		self._Cpblty = value if value is not None else base_types.UninitialisedField(self, 'Cpblty', CardSecurityCapability1Code, False)

	@Cpblty.deleter
	def Cpblty(self):
		del self._Cpblty
		self._Cpblty = base_types.UninitialisedField(self, 'Cpblty', CardSecurityCapability1Code, False)

	@property
	def OthrCpblty(self):
		return self._OthrCpblty

	@OthrCpblty.setter
	def OthrCpblty(self, value):
		self._OthrCpblty = value if value is not None else base_types.UninitialisedField(self, 'OthrCpblty', Max35Text, False)

	@OthrCpblty.deleter
	def OthrCpblty(self):
		del self._OthrCpblty
		self._OthrCpblty = base_types.UninitialisedField(self, 'OthrCpblty', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cpblty', type=CardSecurityCapability1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCpblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))