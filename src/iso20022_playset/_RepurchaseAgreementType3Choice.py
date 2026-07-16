# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GeneralCollateral3
from . import SpecificCollateral2

class RepurchaseAgreementType3Choice(base_types._BaseFieldType):

	__slots__ = ["_GnlColl", "_SpcfcColl"]
	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if value is not None else base_types.UninitialisedField(self, 'GnlColl', GeneralCollateral3, False)

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = base_types.UninitialisedField(self, 'GnlColl', GeneralCollateral3, False)

	@property
	def SpcfcColl(self):
		return self._SpcfcColl

	@SpcfcColl.setter
	def SpcfcColl(self, value):
		self._SpcfcColl = value if value is not None else base_types.UninitialisedField(self, 'SpcfcColl', SpecificCollateral2, False)

	@SpcfcColl.deleter
	def SpcfcColl(self):
		del self._SpcfcColl
		self._SpcfcColl = base_types.UninitialisedField(self, 'SpcfcColl', SpecificCollateral2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GnlColl', type=GeneralCollateral3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SpcfcColl', type=SpecificCollateral2, min=0, max=1, mutex_group=1, array=False),
	))