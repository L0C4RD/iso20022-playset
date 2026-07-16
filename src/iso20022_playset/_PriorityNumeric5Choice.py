# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4NumericText
from . import GenericIdentification47

class PriorityNumeric5Choice(base_types._BaseFieldType):

	__slots__ = ["_Nmrc", "_Prtry"]
	@property
	def Nmrc(self):
		return self._Nmrc

	@Nmrc.setter
	def Nmrc(self, value):
		self._Nmrc = value if value is not None else base_types.UninitialisedField(self, 'Nmrc', Exact4NumericText, False)

	@Nmrc.deleter
	def Nmrc(self):
		del self._Nmrc
		self._Nmrc = base_types.UninitialisedField(self, 'Nmrc', Exact4NumericText, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification47, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification47, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nmrc', type=Exact4NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
	))