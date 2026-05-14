# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionEventType33Code import CorporateActionEventType33Code
from ._GenericIdentification47 import GenericIdentification47

class CorporateActionEventType101Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Prtry"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=CorporateActionEventType33Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
	))