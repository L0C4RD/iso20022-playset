# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification36
from . import ISICIdentifier

class ActivityIndicator1Choice(base_types._BaseFieldType):

	__slots__ = ["_ISICIdr", "_PrtryInd"]
	@property
	def ISICIdr(self):
		return self._ISICIdr

	@ISICIdr.setter
	def ISICIdr(self, value):
		self._ISICIdr = value if value is not None else base_types.UninitialisedField(self, 'ISICIdr', ISICIdentifier, False)

	@ISICIdr.deleter
	def ISICIdr(self):
		del self._ISICIdr
		self._ISICIdr = base_types.UninitialisedField(self, 'ISICIdr', ISICIdentifier, False)

	@property
	def PrtryInd(self):
		return self._PrtryInd

	@PrtryInd.setter
	def PrtryInd(self, value):
		self._PrtryInd = value if value is not None else base_types.UninitialisedField(self, 'PrtryInd', GenericIdentification36, False)

	@PrtryInd.deleter
	def PrtryInd(self):
		del self._PrtryInd
		self._PrtryInd = base_types.UninitialisedField(self, 'PrtryInd', GenericIdentification36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISICIdr', type=ISICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryInd', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))