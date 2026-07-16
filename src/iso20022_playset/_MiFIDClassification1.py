# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import OrderOriginatorEligibility1Code

class MiFIDClassification1(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_Nrrtv"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if value is not None else base_types.UninitialisedField(self, 'Clssfctn', OrderOriginatorEligibility1Code, False)

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = base_types.UninitialisedField(self, 'Clssfctn', OrderOriginatorEligibility1Code, False)

	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if value is not None else base_types.UninitialisedField(self, 'Nrrtv', Max350Text, False)

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = base_types.UninitialisedField(self, 'Nrrtv', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=OrderOriginatorEligibility1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nrrtv', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))