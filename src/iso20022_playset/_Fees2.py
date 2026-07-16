# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Fee7
from . import Max35Text

class Fees2(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_IndvFee"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if value is not None else base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if value is not None else base_types.UninitialisedField(self, 'IndvFee', Fee7, True)

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = base_types.UninitialisedField(self, 'IndvFee', Fee7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvFee', type=Fee7, min=0, max=None, mutex_group=None, array=True),
	))