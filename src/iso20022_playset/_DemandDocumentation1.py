# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document9
from . import Max20000Text
from . import Max2000Text
from . import YesNoIndicator

class DemandDocumentation1(base_types._BaseFieldType):

	__slots__ = ["_CmpltInd", "_CmpltnInf", "_DmndNrrtv", "_NclsdFile"]
	@property
	def CmpltInd(self):
		return self._CmpltInd

	@CmpltInd.setter
	def CmpltInd(self, value):
		self._CmpltInd = value if value is not None else base_types.UninitialisedField(self, 'CmpltInd', YesNoIndicator, False)

	@CmpltInd.deleter
	def CmpltInd(self):
		del self._CmpltInd
		self._CmpltInd = base_types.UninitialisedField(self, 'CmpltInd', YesNoIndicator, False)

	@property
	def CmpltnInf(self):
		return self._CmpltnInf

	@CmpltnInf.setter
	def CmpltnInf(self, value):
		self._CmpltnInf = value if value is not None else base_types.UninitialisedField(self, 'CmpltnInf', Max2000Text, False)

	@CmpltnInf.deleter
	def CmpltnInf(self):
		del self._CmpltnInf
		self._CmpltnInf = base_types.UninitialisedField(self, 'CmpltnInf', Max2000Text, False)

	@property
	def DmndNrrtv(self):
		return self._DmndNrrtv

	@DmndNrrtv.setter
	def DmndNrrtv(self, value):
		self._DmndNrrtv = value if value is not None else base_types.UninitialisedField(self, 'DmndNrrtv', Max20000Text, False)

	@DmndNrrtv.deleter
	def DmndNrrtv(self):
		del self._DmndNrrtv
		self._DmndNrrtv = base_types.UninitialisedField(self, 'DmndNrrtv', Max20000Text, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpltInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndNrrtv', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
	))