# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericIdentification36 import GenericIdentification36
from ._Max4NumericText import Max4NumericText

class Number24Choice(base_types._BaseFieldType):

	__slots__ = ["_NbId", "_Prtry"]
	@property
	def NbId(self):
		return self._NbId

	@NbId.setter
	def NbId(self, value):
		self._NbId = value if type(value) != base_types.auto else self.make_default("NbId")

	@NbId.deleter
	def NbId(self):
		del self._NbId
		self._NbId = None

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
		base_types.FieldEntry(name='NbId', type=Max4NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))