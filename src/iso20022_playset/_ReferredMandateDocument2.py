# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndType1
from . import DocumentType1
from . import Max35Text

class ReferredMandateDocument2(base_types._BaseFieldType):

	__slots__ = ["_CdtrRef", "_Nb", "_RltdDt", "_Tp"]
	@property
	def CdtrRef(self):
		return self._CdtrRef

	@CdtrRef.setter
	def CdtrRef(self, value):
		self._CdtrRef = value if value is not None else base_types.UninitialisedField(self, 'CdtrRef', Max35Text, False)

	@CdtrRef.deleter
	def CdtrRef(self):
		del self._CdtrRef
		self._CdtrRef = base_types.UninitialisedField(self, 'CdtrRef', Max35Text, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@property
	def RltdDt(self):
		return self._RltdDt

	@RltdDt.setter
	def RltdDt(self, value):
		self._RltdDt = value if value is not None else base_types.UninitialisedField(self, 'RltdDt', DateAndType1, False)

	@RltdDt.deleter
	def RltdDt(self):
		del self._RltdDt
		self._RltdDt = base_types.UninitialisedField(self, 'RltdDt', DateAndType1, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', DocumentType1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', DocumentType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDt', type=DateAndType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DocumentType1, min=0, max=1, mutex_group=None, array=False),
	))