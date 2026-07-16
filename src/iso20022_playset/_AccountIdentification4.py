# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SimpleIdentificationInformation1

class AccountIdentification4(base_types._BaseFieldType):

	__slots__ = ["_Prtry"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', SimpleIdentificationInformation1, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', SimpleIdentificationInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=SimpleIdentificationInformation1, min=1, max=1, mutex_group=None, array=False),
	))