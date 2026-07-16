# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralStatus1Code
from . import CollateralStatus2Choice

class TransactionStatus6(base_types._BaseFieldType):

	__slots__ = ["_CvrgSts", "_ExctnSts"]
	@property
	def CvrgSts(self):
		return self._CvrgSts

	@CvrgSts.setter
	def CvrgSts(self, value):
		self._CvrgSts = value if value is not None else base_types.UninitialisedField(self, 'CvrgSts', CollateralStatus1Code, False)

	@CvrgSts.deleter
	def CvrgSts(self):
		del self._CvrgSts
		self._CvrgSts = base_types.UninitialisedField(self, 'CvrgSts', CollateralStatus1Code, False)

	@property
	def ExctnSts(self):
		return self._ExctnSts

	@ExctnSts.setter
	def ExctnSts(self, value):
		self._ExctnSts = value if value is not None else base_types.UninitialisedField(self, 'ExctnSts', CollateralStatus2Choice, False)

	@ExctnSts.deleter
	def ExctnSts(self):
		del self._ExctnSts
		self._ExctnSts = base_types.UninitialisedField(self, 'ExctnSts', CollateralStatus2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CvrgSts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnSts', type=CollateralStatus2Choice, min=0, max=1, mutex_group=None, array=False),
	))