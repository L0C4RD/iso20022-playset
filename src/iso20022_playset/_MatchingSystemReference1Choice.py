# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class MatchingSystemReference1Choice(base_types._BaseFieldType):

	__slots__ = ["_MtchgSysUnqRef", "_RltdRef"]
	@property
	def MtchgSysUnqRef(self):
		return self._MtchgSysUnqRef

	@MtchgSysUnqRef.setter
	def MtchgSysUnqRef(self, value):
		self._MtchgSysUnqRef = value if value is not None else base_types.UninitialisedField(self, 'MtchgSysUnqRef', Max35Text, False)

	@MtchgSysUnqRef.deleter
	def MtchgSysUnqRef(self):
		del self._MtchgSysUnqRef
		self._MtchgSysUnqRef = base_types.UninitialisedField(self, 'MtchgSysUnqRef', Max35Text, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', Max35Text, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RltdRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))