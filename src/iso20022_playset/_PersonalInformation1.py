# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class PersonalInformation1(base_types._BaseFieldType):

	__slots__ = ["_MdnNmOfMthr", "_NmOfFthr", "_NmOfPrtnr"]
	@property
	def MdnNmOfMthr(self):
		return self._MdnNmOfMthr

	@MdnNmOfMthr.setter
	def MdnNmOfMthr(self, value):
		self._MdnNmOfMthr = value if value is not None else base_types.UninitialisedField(self, 'MdnNmOfMthr', Max35Text, False)

	@MdnNmOfMthr.deleter
	def MdnNmOfMthr(self):
		del self._MdnNmOfMthr
		self._MdnNmOfMthr = base_types.UninitialisedField(self, 'MdnNmOfMthr', Max35Text, False)

	@property
	def NmOfFthr(self):
		return self._NmOfFthr

	@NmOfFthr.setter
	def NmOfFthr(self, value):
		self._NmOfFthr = value if value is not None else base_types.UninitialisedField(self, 'NmOfFthr', Max35Text, False)

	@NmOfFthr.deleter
	def NmOfFthr(self):
		del self._NmOfFthr
		self._NmOfFthr = base_types.UninitialisedField(self, 'NmOfFthr', Max35Text, False)

	@property
	def NmOfPrtnr(self):
		return self._NmOfPrtnr

	@NmOfPrtnr.setter
	def NmOfPrtnr(self, value):
		self._NmOfPrtnr = value if value is not None else base_types.UninitialisedField(self, 'NmOfPrtnr', Max35Text, False)

	@NmOfPrtnr.deleter
	def NmOfPrtnr(self):
		del self._NmOfPrtnr
		self._NmOfPrtnr = base_types.UninitialisedField(self, 'NmOfPrtnr', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MdnNmOfMthr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmOfFthr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmOfPrtnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))