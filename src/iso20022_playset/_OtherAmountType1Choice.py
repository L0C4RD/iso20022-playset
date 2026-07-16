# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1
from . import OtherAmountType1Code

class OtherAmountType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_PrtryCd"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', OtherAmountType1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', OtherAmountType1Code, False)

	@property
	def PrtryCd(self):
		return self._PrtryCd

	@PrtryCd.setter
	def PrtryCd(self, value):
		self._PrtryCd = value if value is not None else base_types.UninitialisedField(self, 'PrtryCd', GenericIdentification1, False)

	@PrtryCd.deleter
	def PrtryCd(self):
		del self._PrtryCd
		self._PrtryCd = base_types.UninitialisedField(self, 'PrtryCd', GenericIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=OtherAmountType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryCd', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))